import Api from '@/service/api'

class Data {
  constructor() {
    this.request = Api
  }

  getData(skip = 0, limit = 10) {
    return this.request.get('/data/?skip={skip}&limit=${limit}')
  }

  createData(data) {
    return this.request.post('/data', data)
  }

  updateData(dataId, payload) {
    return this.request.patch(`/data/${dataId}`, payload)
  }

  deleteDataset(dataId) {
    return this.request.delete(`/data/${dataId}`)
  }

  fetchDatasetById(dataId) {
    return this.request.get(`/data/${dataId}`)
  }
}

export default new Data()