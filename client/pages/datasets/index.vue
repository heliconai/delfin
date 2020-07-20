<template>
  <div>
    <card
      class="has-table has-mobile-sort-spaced"
    >
      <data-table
        :data-url="'http://localhost:3000/clients.json'"
        :checkable="true"
        :striped="false"
        :hoverable="true"
        :per-page="20"
        :loading=false
        :paginated=true
      />
    </card>
  </div>
</template>

<script>
import Card from '@/components/common/Card'
import DataTable from '@/components/datasets/DataTable'
export default {
  layout: 'datasets',
  components: {Card, DataTable}
}
</script>

<style>
</style>