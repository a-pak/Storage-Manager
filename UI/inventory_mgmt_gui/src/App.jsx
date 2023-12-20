import ProductTable from "./Components/Table"
import Header from "./Components/Header"
import ProductForm from "./Components/ProductForm"
import { Grid } from "@mui/material"
import dbservice from './Services/dbservice';
import { useEffect, useState } from "react"

function App() {

  const [products, setProducts] = useState([])
  
  useEffect(() => {
    console.log('getting stock...')
    dbservice
      .getAll()
      .then(response => {
        setProducts(response.data.data || [])
        console.log('...stock set succesfully')
      })
      .catch(err => console.error('Error fetching stock:', err))
  }, [])

  return (
    <>
    <Grid container spacing={2} >
      <Grid item sx={{marginLeft:2, marginRight:2}}>
        <Header />
      </Grid>
      <Grid item alignContent={"center"} sx={{marginTop:4}}>
        <ProductForm products={products} setProducts={setProducts}/>
      </Grid>
      <Grid item xs={12} >
        <ProductTable products={products} setProducts={setProducts}/> 
      </Grid>
    </Grid>
    </>
  )
}

export default App
