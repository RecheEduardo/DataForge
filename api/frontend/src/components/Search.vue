<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const query = ref<string>('Filantropia')

const search = async (): Promise<void> => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/search?query=${query.value}`)
    console.log('Resposta da API:', response.data)
  } catch (error) {
    console.error('Erro ao buscar dados:', error)
  }
}
</script>

<template>
  <div>
    <button @click="search" class="btn btn-lg btn-primary">Buscar</button>
  </div>
</template>