<template>
  <div>
    <h1 class="title">Data Sets</h1>
    <card
      class="has-table has-mobile-sort-spaced"
      title="Clients"
      icon="account-multiple"
    >
      <data-table
        :data-url="'http://localhost:3000/clients.json'"
        :checkable="true"
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