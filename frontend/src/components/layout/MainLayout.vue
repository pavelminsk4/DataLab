<template>
  <div
    :class="['main-layout-wrapper', isProjectExtraSettings && 'extra-settings']"
  >
    <BackgroundIcon class="background-icon" />
    <div class="content">
      <MainHeader :is-visible-logo="isVisibleLogo" />

      <slot></slot>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import MainHeader from '@components/navigation/MainHeader'
import BackgroundIcon from '@/components/icons/BackgroundIcon'

export default {
  name: 'MainLayout',
  components: {
    BackgroundIcon,
    MainHeader,
  },
  props: {
    isProjectExtraSettings: {
      type: Boolean,
      default: false,
    },
    isVisibleLogo: {
      type: Boolean,
      default: true,
    },
  },
  created() {
    if (!Object.keys(this.userInfo).length) {
      this[action.GET_USER_INFORMATION]()
    }
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  computed: {
    ...mapGetters({workspaces: get.WORKSPACES, userInfo: get.USER_INFO}),
  },
  methods: {
    ...mapActions([action.GET_USER_INFORMATION, action.GET_WORKSPACES]),
  },
}
</script>

<style lang="scss" scoped>
.main-layout-wrapper {
  position: relative;

  padding: 0 69px 100px 79px;
}

.extra-settings {
  padding: 0 69px 100px 124px;
}

.background-icon {
  position: absolute;
  right: 50%;
  left: 50%;
  transform: translate(-50%, 0);

  max-height: 100vh;

  z-index: -1;
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

@media (max-width: 800px) {
  .main-layout-wrapper {
    position: relative;

    padding: 0 30px 130px 30px;
  }
}
</style>
