<template>
  <router-view></router-view>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

const {mapActions, mapGetters} = createNamespacedHelpers('online')

export default {
  name: 'OnlineModuleView',
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
  },
  created() {
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
  },
}
</script>
