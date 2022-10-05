<template>
  <div class="main-layout-wrapper">
    <BackgroundIcon class="background-icon" />
    <div class="content">
      <MainHeader />

      <slot></slot>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import MainHeader from '@components/navigation/MainHeader'
import BackgroundIcon from '@/components/icons/BackgroundIcon'

export default {
  name: 'MainLayout',
  components: {
    BackgroundIcon,
    MainHeader,
  },
  created() {
    if (!Object.keys(this.userInfo).length) {
      this[action.GET_USER_INFORMATION]()
    }
  },
  computed: {
    ...mapState(['userInfo']),
  },
  methods: {
    ...mapActions([action.LOGOUT, action.GET_USER_INFORMATION]),
  },
}
</script>

<style lang="scss" scoped>
.main-layout-wrapper {
  position: relative;

  padding: 0 69px 160px 79px;
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
