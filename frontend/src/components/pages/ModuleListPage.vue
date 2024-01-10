<script setup lang="ts">
import PageHeader from '../PageHeader.vue'

import { ref, onMounted } from 'vue'
import axios from 'axios'

import 'datatables.net-bs5'
import DataTable from 'datatables.net-vue3'
import DataTablesCore from 'datatables.net'

DataTable.use(DataTablesCore)

interface AnimalFacts {
  text: string
}

const data = ref<AnimalFacts[]>([])
const columns = [
  {
    data: 'text',
    title: 'First'
  }

]

async function fetchCatFacts () {
  const catFactsResponse = await axios.get<AnimalFacts[]>('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5')
  catFactsResponse.data.forEach(f => data.value.push(f))
}

onMounted(async () => { await fetchCatFacts() })
</script>

<template>
  <PageHeader title="Wowee">
    Hey
  </PageHeader>

  <div class="container-fluid my-5">
    <div class="row align-items-center">
      <div class="col-xl-9 toggles-ignore mx-auto">
        <DataTable
          ref="table"
          :data="data"
          :columns="columns"
          class="display table table-striped table-bordered"
        />
      </div>
    </div>
  </div>
</template>
