import Vue from 'vue'
import moment from 'moment'

Vue.filter('formatDateTime', value => {
    if (!value) return ''
    return moment(value).format('MMMM Do YYYY, h:mm a');
})