import Api from '@/service/api'

class annotationTypes {
  constructor() {
    this.request = Api
  }

  getAnnotationTypesList() {
    return this.request.get('/annotation_types/?skip={skip}&limit=${limit}')
  }

  createAnnotationType(data) {
    return this.request.post('/annotation_types/', data)
  }

  updateAnnotationType(annotationTypeId, payload) {
    return this.request.patch(`/annotation_types/${annotationTypeId}`, payload)
  }

  deleteAnnotationType(annotationTypeId) {
    return this.request.delete(`/annotation_types/${annotationTypeId}`)
  }

  fetchAnnotationTypeById(annotationTypeId) {
    return this.request.get(`/annotation_types/${annotationTypeId}`)
  }
}

export default new annotationTypes()