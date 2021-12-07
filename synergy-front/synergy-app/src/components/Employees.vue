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
    AAAA<div v-for="occupation in occupations" :key="occupation.id">qweqwe{{occupation.name}}</div>VVV
    

  </v-card>
</template>

<script>
    import gql from 'graphql-tag'
    export default {
        data: () => ({
            name: "asd",
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
        apollo: {occupations: gql`query {occupations {id, name, companyName, positionName}}`},
  }
</script>
