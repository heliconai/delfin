
import Api from '@/service/api'

class dataModality {
  constructor() {
    this.request = Api
  }

  getDataModalityList() {
    return this.request.get('/data_modality/?skip={skip}&limit=${limit}')
  }

  createDataModality(data) {
    return this.request.post('/data_modality', data)
  }

  updateDataModality(dataModalityId, payload) {
    return this.request.patch(`/data_modality/${dataModalityId}`, payload)
  }

  deleteDataModality(dataModalityId) {
    return this.request.delete(`/data_modality/${dataModalityId}`)
  }

  fetchDataModalityById(dataModalityId) {
    return this.request.get(`/data_modality/${dataModalityId}`)
  }
}

export default new dataModality()