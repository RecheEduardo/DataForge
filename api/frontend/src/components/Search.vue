<script setup lang="ts">
    import { ref } from 'vue'
    import axios from 'axios'

    // interface para garantir a tipagem correta
    // dos dados vindos da API
    interface Operadora {
    Razao_Social: string
    Cidade: string
    UF: string
    }

    // variavel que vai receber qual dado o usuario irá filtrar
    const query = ref<string>('')

    // vai receber o resultado da requisição como um 
    // array de elementos da interface "Operadora"
    const results = ref<Operadora[]>([])

    const search = async (): Promise<void> => {
        try {
            // requisição http feita para a rota da API
            const response = await axios.get(`http://127.0.0.1:5000/search?query=${query.value}`)

            let data = response.data
            // verifica se o dado recebido é um array. Caso não seja, tenta extrair os itens.
            if (!Array.isArray(data)) {
            // se a resposta for um objeto, por exemplo { resultado: [...] }
            // vai tentar acessar a propriedade correta ou converta o objeto para array
            data = data.results || Object.values(data)
            }
            
            // mapeia os dados para garantir que todas as props necessarias existe
            results.value = data.map((item: any) => ({
            Razao_Social: item.Razao_Social || item.razao_social || '',
            Cidade: item.Cidade || item.cidade || '',
            UF: item.UF || item.uf || ''
            }))
        } catch (error) {
            console.error('Erro ao buscar dados:', error)
        }
    }
</script>

<template>
  <div class="container my-5">
    <div class="input-group mb-3">
        <input type="text" v-model="query" placeholder="Modalidade do cadastro..." class="form-control fs-5" aria-label="Recipient's username" aria-describedby="button-addon2">
        <button class="btn btn-success fw-bold fs-5" @click="search" type="button" id="button-addon2">Buscar</button>
    </div>
    <!-- tabela aonde os elementos irão ser exibidos -->
    <table class="table table-hover table-striped">
        <thead class="table-dark">
            <tr>
                <th scope="col">#</th>
                <th scope="col">Razão Social</th>
                <th scope="col">Cidade</th>
                <th scope="col">UF</th>
            </tr>
        </thead>
        <tbody>
        <!-- loop de iteração acessa e exibe os dados da interface -->
            <tr v-for="(item, index) in results" :key="index">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ item.Razao_Social }}</td>
                <td>{{ item.Cidade }}</td>
                <td>{{ item.UF }}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>