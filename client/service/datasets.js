import Api from '@/service/api'

class Datasets {
  constructor() {
    this.request = Api
  }

  getDatasets(skip = 0, limit = 10) {
    return this.request.get('/datasets/')//?skip={skip}&limit=${limit}')
  }

  createDataset(data) {
    return this.request.post('/datasets', data)
  }

  updateDataset(datasetId, payload) {
    return this.request.patch(`/datasets/${datasetId}`, payload)
  }

  deleteDataset(datasetId) {
    return this.request.delete(`/datasets/${datasetId}`)
  }

  fetchDatasetById(datasetId) {
    return this.request.get(`/datasets/${datasetId}`)
  }
}

export default new Datasets()