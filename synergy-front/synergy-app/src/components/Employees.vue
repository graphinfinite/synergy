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
    <v-data-table :headers="headers" :items="occupations" :search="search" fixed-header>
      <template #item="{ item }">
        <tr v-if="show_dismissed || !(item.fireDate!=null)" :class="item.fireDate!=null ? 'rowstyle-1' : 'rowstyle-2'">
          <td>
            <v-checkbox v-if="item.fireDate===null" input-value=""></v-checkbox>
          </td>
          <td>{{item.name}}</td>
          <td>{{item.companyName}}</td>
          <td>{{item.positionName}}</td>
          <td>{{item.hireDate}}</td>
          <td>{{item.fireDate}}</td>
          <td>{{item.salary}}</td>
          <td>{{item.base}}</td>
          <td>{{item.advance}}</td>
          <td>
            <v-checkbox input-value=""></v-checkbox>{{item.byHours}}
          </td>
        </tr> 
      </template>

      <template v-slot:top>
        <v-toolbar flat color=#e0ccff>
          <v-spacer></v-spacer>
          <div class="d-flex w-100">
            <v-checkbox color=#751aff label="Показывать уволенных" v-model="show_dismissed"></v-checkbox>
            <v-btn
              color=#751aff
              class="ml-2 white--text"
              @click="addNewEmployee">
              <v-icon dark>mdi-plus</v-icon>Принять на должность
            </v-btn>
            <v-btn
              disabled
              color=#751aff
              class="ml-2 white--text"
              @click="fireEmployee">
              <v-icon dark>mdi-minus</v-icon>Снять с должности
            </v-btn> 
          </div>
        </v-toolbar>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import { GET_OCCUPATIONS } from '@/graphql'

export default {
  data: () => ({
      occupations: [],
      show_dismissed: false,
      search: '',
      headers: [
          { text: '', value: 'choice' },
          {
            text: 'Сотрудник',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Компания', value: 'companyName' },
          { text: 'Должность', value: 'positionName' },
          { text: 'Дата приема', value: 'hireDate' },
          { text: 'Дата увольнения', value: 'fireDate' },
          { text: 'Ставка', value: 'salary' },
          { text: 'База', value: 'base' },
          { text: 'Аванс', value: 'advance' },
          { text: 'Почасовая', value: 'byHours' },
      ],
    }), 
  apollo: {
    $loadingKey: 'loading',
    occupations:{query: GET_OCCUPATIONS}
    },
  methods: {
    addNewEmployee: function(event) {
      console.log(event)
    },
    fireEmployee: function(event) {
      console.log(event)
    },
  }
        
}
</script>


<style scoped>
.rowstyle-1 {
  background-color: rgb(224, 17, 17)
}
.rowstyle-2 {
  background-color: rgb(248, 244, 244)
}
</style>

