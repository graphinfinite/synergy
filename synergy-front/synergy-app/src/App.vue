<template>
  <v-app>
    <v-main>
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
