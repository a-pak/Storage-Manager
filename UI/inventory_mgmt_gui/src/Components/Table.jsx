import { Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import dbservice from '../Services/dbservice';
import { useEffect, useState } from "react"

const ProductTable = ({ products, setProducts }) => {


  const orderProduct = product => {
    dbservice
      .order(product.id)
      .then(() => {
          setProducts(prevProducts => prevProducts.filter(p => p.id !== product.id))
      })
      .catch(err => console.error('Error ordering the product:', err))
  }


  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Description</TableCell>
            <TableCell>Location</TableCell>
            <TableCell>Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {products.length !== 0 
          ? (products.map((product) => (
            <TableRow key={product.id}>
            <TableCell>{product.name}</TableCell>
            <TableCell>{product.description}</TableCell>
            <TableCell>{product.location}</TableCell>
              <TableCell>
                <Button variant="contained" color="primary" onClick={() => orderProduct(product)}>
                  Order
                </Button>
              </TableCell>
            </TableRow>
          ))) : ( 
          <TableCell>Warehouse is currently empty</TableCell> 
            )}
          </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ProductTable;
