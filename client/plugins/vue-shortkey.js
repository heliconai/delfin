import Vue from 'vue'
const ShortKey = require('vue-shortkey')

// from https://github.com/iFgR/vue-shortkey/blob/master/README.md#integrating-with-nuxt
Vue.use(ShortKey, { prevent: ['input', 'textarea'] })

export default ShortKey