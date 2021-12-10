<template>
  <v-app>
    <v-main  class="back-ground-total">
      <Employees/>
    </v-main>
  </v-app>
</template>

<script>
import Employees from './components/Employees';

export default {
  name: 'App',
  components: {
    Employees
  },

  data: () => ({
    //
  }),
};
</script>




<style scoped>
.back-ground-total {
  background-color:#e0ccff;
}
</style>
