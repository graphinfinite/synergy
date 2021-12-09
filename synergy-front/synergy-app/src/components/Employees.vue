<template>
  <v-card>

    <v-card-title>
        
      Занимаемые должности
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Поиск по сотруднику"
        single-line
      ></v-text-field>

    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="occupations"
      :search="search"
    ></v-data-table>
    AAA<div v-for="occupation in occupations" :key="occupation.id">{{occupation.name}}</div>VVV
    

  </v-card>
</template>

<script>
    import { GET_OCCUPATIONS } from '@/graphql'

    export default {
        data: () => ({
            occupations: [],
            search: '',
            headers: [
                {
                    text: 'Сотрудник',
                    align: 'start',
                    sortable: false,
                    value: 'name',
                },
                { text: 'Компания', value: 'company_name' },
                { text: 'Должность', value: 'position_name' },
                { text: 'Дата приема', value: 'hire_date' },
                { text: 'Дата увольнения', value: 'fire_date' },
                { text: 'Ставка', value: 'salary' },
                { text: 'База', value: 'base' },
                { text: 'Аванс', value: 'avance' },
                { text: 'Почасовая', value: 'by_hours' },
                { text: 'Почасовая', value: 'advance' },
            ],
          }),
        
        apollo: {
          $loadingKey: 'loading',
          
          occupations:{query: GET_OCCUPATIONS}
          }
        
  }
</script>
