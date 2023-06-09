<template>
  <div>WokspaceView</div>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

export default {
  name: 'ComparisonModuleView',
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
  },
}
</script>
