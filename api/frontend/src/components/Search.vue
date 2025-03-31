<script setup lang="ts">
    import { ref, computed } from 'vue'
    import axios from 'axios'

    // interface para garantir a tipagem correta
    // dos dados vindos da API
    interface Operadora {
        Representante: string
        Razao_Social: string
        Modalidade: string
        Cidade: string
        UF: string
    }

    // variavel que vai receber qual dado o usuario irá filtrar
    const query = ref<string>('')

    // a pesquisa padrao começa com modalidade
    const searchType = ref<string>('modalidade')

    // variavel de controle para saber se esta carregando
    const loading = ref<boolean>(false)

    // vai receber o resultado da requisição como um 
    // array de elementos da interface "Operadora"
    const results = ref<Operadora[]>([])


    // uso do computed para mudar o placeholder do input
    // conforme alteração do option
    const placeholderText = computed(() => {
        switch (searchType.value) {
            case 'modalidade':
            return 'Digite a modalidade desejada...'
            case 'uf':
            return 'Informe o estado (ex: SP, RJ, MG)...'
            case 'representante':
            return 'Pesquise pelo nome do representante..'
            default:
            return 'Digite sua pesquisa...'
        }
    })

    const cleanUp = (): void => {
        results.value = []
        query.value = ''
    }

    const search = async (): Promise<void> => {

        loading.value = true 

        let endpoint: string = ''
        if (searchType.value === 'modalidade') {
            endpoint = 'http://127.0.0.1:5000/searchModalidade'
        } else if (searchType.value === 'uf') {
            endpoint = 'http://127.0.0.1:5000/searchUF'
        } else if (searchType.value === 'representante') {
            endpoint = 'http://127.0.0.1:5000/searchRepresentante'
        }

        try {
            // requisição http feita para a rota da API
            const response = await axios.get(`${endpoint}?query=${query.value}`)

            let data = response.data
            // verifica se o dado recebido é um array. Caso não seja, tenta extrair os itens.
            if (!Array.isArray(data)) {
            // se a resposta for um objeto, por exemplo { resultado: [...] }
            // vai tentar acessar a propriedade correta ou converta o objeto para array
                data = data.results || Object.values(data)
            }
            
            // mapeia os dados para garantir que todas as props necessarias existem
            results.value = data.map((item: any) => ({
                Razao_Social: item.Razao_Social || item.razao_social || '',
                Cidade: item.Cidade || item.cidade || '',
                UF: item.UF || item.uf || '',
                Representante: item.Representante || item.representante || '',
                Modalidade: item.Modalidade || 
                item.modalidade || ''
            }))
        } catch (error) {
            console.error('Erro ao buscar dados:', error)
        } finally {
            loading.value = false
        }
    }
</script>

<template>
  <div class="container popUp">

    <!-- opcao de selecionar o tipo de busca -->
    <div class="pb-3 mb-3 border-bottom">
        <div class="d-flex justify-content-between align-items-center border-bottom mt-4 mb-3">
            <h1 class="text-muted mb-3 fadeInUp">Busca de cadastros</h1>
            <button class="btn fs-4 btn-secondary text-light fw-bold" @click="cleanUp">Limpar</button>
        </div>
        <select v-model="searchType" class="form-select fs-5 fadeInUp">
            <option value="modalidade">Modalidade</option>
            <option value="uf">UF</option>
            <option value="representante">Representante</option>
        </select>
    </div>

    <!-- campo de pesquisa da consulta -->
    <div class="input-group mb-3 popIn">
        <input type="text" v-model="query" :placeholder="placeholderText" id="search-bar" class="form-control fs-4" aria-label="Search query">
        <button class="btn btn-success fw-bold fs-4" @click="search" type="button">
        <i class="fa-solid fa-magnifying-glass"></i>
        Buscar
        </button>
    </div>

    <!-- tela de loading durante a busca -->
    <div v-if="loading">
        <p class="text-muted text-center fs-1">Carregando...</p>
    </div>

    <!-- tabela aonde os elementos irao ser exibidos no final da busca -->
    <div v-else-if="results.length">
        <table class="table table-hover table-striped table-bordered popUp">
            <thead class="table-dark">
                <tr>
                    <th scope="col">
                        <i class="fa-solid fa-hashtag"></i>
                    </th>
                    <th scope="col">
                        <i class="fa-solid fa-user"></i>
                        Representante
                    </th>
                    <th scope="col">Razão Social</th>
                    <th scope="col">Modalidade</th>
                    <th scope="col">
                        <i class="fa-solid fa-map-location-dot"></i>
                        Cidade
                    </th>
                    <th scope="col">UF</th>
                </tr>
            </thead>

            <tbody>
            <!-- loop de iteração acessa e exibe os dados da interface -->
                <tr v-for="(item, index) in results" :key="index">
                    <th scope="row">{{ index + 1 }}</th>
                    <td>{{ item.Representante }}</td>
                    <td>{{ item.Razao_Social }}</td>
                    <td>{{ item.Modalidade }}</td>
                    <td>{{ item.Cidade }}</td>
                    <td>{{ item.UF }}</td>
                </tr>
            </tbody>
        </table>
    </div>

  </div>
</template>