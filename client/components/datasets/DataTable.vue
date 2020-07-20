<!-- TODO make data table columns correct -->
<!-- TODO move data retrieval to services and stores -->
<template>
  <div>
    <b-table
      :checked-rows="selected"
      :checkable="checkable"
      :loading="loading"
      :paginated="paginated"
      :per-page="perPage"
      :striped="striped"
      :hoverable="hoverable"
      default-sort="name"
      :data="empty ? [] : datasets"
      @check="updateSelection"
    >
      <template slot-scope="props">
        <b-table-column class="has-no-head-mobile is-image-cell">
          <div class="image">
            <img :src="props.row.avatar" class="is-rounded" />
          </div>
        </b-table-column>
        <b-table-column label="Dataset Name" field="name" sortable><nuxt-link :to="`/datasets/${props.row.id}`">{{ props.row.name }}</nuxt-link></b-table-column>
        <b-table-column label="Created On" field="created_on" sortable>{{ props.row.created_on | formatDateTime }}</b-table-column>
        <b-table-column label="Updated On" field="updated_on" sortable>{{ props.row.updated_on | formatDateTime }}</b-table-column>
        <b-table-column custom-key="actions" sticky class="is-actions-cell">
          <div class="buttons is-right">
            <nuxt-link :to="`/datasets/${props.row.id}/admin`" class="button is-info">
            <i class="material-icons mr-1">settings</i>
            Admin
            </nuxt-link>
            <nuxt-link :to="`/datasets/${props.row.id}`" class="button">
            <i class="material-icons mr-1">perm_media</i>
            Data
            </nuxt-link>
          </div>
        </b-table-column>
      </template>

      <template v-if="!loading" slot="empty">
        <section class="section">
          <div class="content has-text-grey has-text-centered">
            <p>
              <i class="material-icons md-48">info</i>
            </p>
            <p>No Datasets Available&hellip;</p>
          </div>
        </section>
      </template>
    </b-table>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions, mapMutations } from 'vuex'
export default {
  name: 'DataTable',
  props: {
    dataUrl: {
      type: String,
      default: null
    },
    striped : {
      type: Boolean,
      default: false
    },
    hoverable : {
      type: Boolean,
      default: true
    },
    checkable : {
      type: Boolean,
      default: true
    },
    paginated : {
      type: Boolean,
      default: true
    },
    perPage : {
      type: Number,
      default : 20
    }
    },
  computed: {
    ...mapState('datasets', ['datasets', 'selected', 'loading', 'empty'])

  },
  created() {
    this.getDatasetList()
  },
  methods: {
    ...mapActions('datasets', ['getDatasetList']),
    ...mapMutations('datasets', ['updateSelected']),

    updateSelection(selected) {
      this.updateSelected(selected)
    }
    }
}
</script>