<template>
  <div class="main-layout">
    <MainHeader />
    <section class="two-columns-wrapper">
      <div class="content">
        <slot></slot>
      </div>

      <div v-if="isTwoColumns" class="second-column">
        <slot name="second-column"></slot>
      </div>
    </section>
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
    isTwoColumns: {
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

<style lang="scss">
.main-layout {
  position: relative;

  display: flex;

  padding-top: var(--header-height);
  width: 100vw;
  height: 100vh;

  &__section {
    width: 100%;
  }
}
</style>

<style lang="scss" scoped>
.two-columns-wrapper {
  display: flex;

  width: 100%;
}

.second-column {
  width: 100%;

  background-color: var(--background-secondary-color);
}

.content {
  z-index: 2;

  width: 100%;
  padding: 24px 32px;
}
</style>
