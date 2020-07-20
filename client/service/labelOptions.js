import Api from '@/service/api'

class labelOptions {
  constructor() {
    this.request = Api
  }

  getLabelOptionsList() {
    return this.request.get('/label_options/?skip={skip}&limit=${limit}')
  }

  createLabelOption(data) {
    return this.request.post('/label_options/', data)
  }

  updateLabelOption(labelOptionId, payload) {
    return this.request.patch(`/label_options/${labelOptionId}`, payload)
  }

  deleteLabelOption(labelOptionId) {
    return this.request.delete(`/label_options/${labelOptionId}`)
  }

  fetchLabelOptionById(labelOptionId) {
    return this.request.get(`/label_options/${labelOptionId}`)
  }
}

export default new labelOptions()