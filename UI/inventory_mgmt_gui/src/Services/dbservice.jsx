import axios from 'axios'
const baseUrl = 'http://localhost:5000/api/stock';

const getAll = () => {
  return axios.get(baseUrl)
}
const create = object => {
  return axios.post(baseUrl, object)
}
const order = id => {
  return axios.delete(`${baseUrl}/${id}`)
}

export default { getAll, create, order }