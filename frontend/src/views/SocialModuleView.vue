<template>
  <router-view></router-view>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/modules/social/constants'

const {mapActions, mapGetters} = createNamespacedHelpers('social')

export default {
  name: 'SocialModuleView',
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
