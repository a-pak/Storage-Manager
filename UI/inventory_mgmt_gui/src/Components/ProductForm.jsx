import { useState, } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import TextField from '@mui/material/TextField';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import dbservice from '../Services/dbservice';

const ProductForm = ({ products, setProducts }) => {
  const [open, setOpen] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    location: 1, // Default value for location
  });
  const [freeLocations, setFreeLocations] = useState([1, 2, 3, 4, 5, 6, 7, 8, 9])

  const handleClickOpen = () => {
    setOpen(true);
    const usedLocations = products.map(product => product.location)
    const newFreeLocations = freeLocations.filter(location => !usedLocations.includes(location));
    setFreeLocations(newFreeLocations);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLocationChange = (e) => {
    setFormData({
      ...formData,
      location: e.target.value,
    });
  };
  
  const handleFormSubmit = async () => {
    try {
      // Handle form submission logic here
      const response = await dbservice.create(formData);
  
      // Update formData with the received ID
      setFormData(prevFormData => ({
        ...prevFormData,
        id: response.data.id,
      }));
      
      console.log('Form submitted with response:', response);
  
      // Update the products state with the new product, using the updated formData
      setProducts(prevProducts => [...prevProducts, formData ]);
  
      // Close the dialog
      handleClose();
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <div>
      <Button variant="contained" onClick={handleClickOpen} sx={{m:2}}>
        Add Item
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Add Product</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Please fill out the form to add a new product.
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            label="Name"
            type="text"
            name="name"
            fullWidth
            onChange={handleInputChange}
          />
          <TextField
            margin="dense"
            label="Description"
            type="text"
            name="description"
            fullWidth
            onChange={handleInputChange}
          />
          <br />
          <FormControl fullWidth sx={{pt:3}}>
            <InputLabel sx={{pt:2}} id="location-label">Location</InputLabel>
            <Select
              labelId="location-label"
              id="location"
              name="location"
              value={formData.location}
              onChange={handleLocationChange}
            >
              {freeLocations.map((location) => (
                <MenuItem key={location} value={location}>
                  {location}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Cancel
          </Button>
          <Button onClick={handleFormSubmit} color="primary">
            Add
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default ProductForm;
