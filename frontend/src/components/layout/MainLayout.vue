<template>
  <div class="main-layout-wrapper">
    <MainHeader />
    <div class="content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import MainHeader from '@components/navigation/MainHeader'

export default {
  name: 'MainLayout',
  components: {
    MainHeader,
  },
  props: {
    isProjectExtraSettings: {
      type: Boolean,
      default: false,
    },
  },
  created() {
    if (!this.userInfo) {
      this[action.GET_USER_INFORMATION]()
    }

    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      userInfo: get.USER_INFO,
    }),
  },
  methods: {
    ...mapActions([action.GET_USER_INFORMATION, action.GET_WORKSPACES]),
  },
}
</script>

<style lang="scss" scoped>
.main-layout-wrapper {
  position: relative;

  padding: var(--header-height) 40px 50px 70px;
}

.extra-settings {
  padding: 0 69px 0 124px;
}

.content {
  z-index: 2;
}

.bg-icon {
  position: absolute;
  top: 40%;
  left: 50%;

  width: 66vw;

  z-index: 1;
  transform: translate(-50%, -50%);
}
</style>
