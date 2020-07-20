import Datasets from '@/service/datasets'

export const state = () => ({
  datasets: [],
  selected: [],
  skip: 0,
  limit: 10,
  current: {},
  loading: false,
  empty: false
})

export const getters = {
  isAnyDatasetSelected(state) {
    return state.selected.length > 0
  },
  currentDataset(state) {
    return state.current
  },
}

export const mutations = {
  setDatasetList(state, payload) {
    state.datasets = payload
  },
  createDataset(state, dataset) {
    state.datasets.unshift(dataset)
  },
  updateDataset(state, dataset) {
    const item = state.dataset.find((item) => item.id === dataset.id)
    Object.assign(item, dataset)
  },
  deleteDataset(state, datasetId) {
    state.datasets = state.datasets.filter((item) => item.id !== datasetId)
  },
  updateSelected(state, selected) {
    state.selected = selected
  },
  resetSelected(state) {
    state.selected = []
  },
  setLoading(state, payload) {
    state.loading = payload
  },
  setCurrent(state, payload) {
    state.current = payload
  },
  setEmpty(state, payload) {
    state.empty = payload
  }
}

export const actions = {
  getDatasetList({ commit }) {
    commit('setLoading', true)
    commit('setEmpty', false)
    Datasets.getDatasets()
      .then((response) => {
        commit('setDatasetList', response.data)
      })
      .catch((error) => {
        alert(error)
      })
      .finally(() => {
        commit('setLoading', false)
      })
  },
  createDataset({ commit }, dataset) {
    Datasets.createDataset(dataset)
      .then((response) => {
        commit('createDataset', response.data)
      })
      .catch((error) => {
        alert(error)
      })
  },
  updateDataset({ commit }, data) {
    Datasets.updateDataset(data.datasetId, data)
      .then((response) => {
        commit('updateDataset', response.data)
      })
      .catch((error) => {
        alert(error)
      })
  },
  deleteDataset({ commit, state }) {
    for (const dataset of state.selected) {
      Dataset.deleteDataset(dataset.id)
        .then((response) => {
          commit('deleteDataset', dataset.id)
        })
        .catch((error) => {
          alert(error)
        })
    }
    commit('resetSelected')
  },
  setCurrentDataset({ commit }, datasetId) {
    return Dataset.fetchDatasetById(datasetId)
      .then((response) => {
        commit('setCurrent', response.data)
      })
      .catch((error) => {
        alert(error)
      })
  },
  updateCurrentDataset({ commit }, data) {
    Dataset.updateDataset(data.datasetId, data)
      .then((response) => {
        commit('setCurrent', response.data)
      })
      .catch((error) => {
        alert(error)
      })
  },
}
