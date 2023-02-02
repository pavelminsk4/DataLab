<template>
  <nav class="settings-nav-wrapper">
    <li
      v-for="(item, index) in settings"
      :key="'setting' + index"
      :class="['nav-item', item === routeName && 'active-setting']"
      @click="$emit('open-tab', item)"
    >
      <component
        :is="item + 'Icon'"
        :class="[item === routeName && 'active-icon']"
      />

      <div>{{ item }}</div>
    </li>
  </nav>
</template>

<script>
import AnalyticsIcon from '@/components/icons/AnalyticsIcon'
import SearchIcon from '@/components/icons/SearchIcon'
import AlertsIcon from '@/components/icons/AlertsIcon'
import ReportsIcon from '@/components/icons/ReportsIcon'

export default {
  name: 'SideBar',
  components: {
    AlertsIcon,
    SearchIcon,
    ReportsIcon,
    AnalyticsIcon,
  },
  data() {
    return {
      settings: ['Analytics', 'Search', 'Alerts', 'Reports'],
    }
  },
  computed: {
    routeName() {
      return this.$route.name
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-nav-wrapper {
  --padding-top: calc(var(--header-height) + 24px);

  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;

  display: flex;
  flex-direction: column;
  align-items: center;

  width: 210px;
  height: 100vh;
  padding: var(--padding-top) 24px 20px 12px;

  border-right: 1px solid var(--border-color);
  background-color: var(--background-secondary-color);

  .nav-item {
    display: flex;
    align-items: center;

    width: 172px;
    height: 44px;
    padding: 12px 16px;
    margin-bottom: 10px;

    cursor: pointer;

    font-style: normal;
    font-weight: 500;
    font-size: 16px;
    line-height: 20px;
    color: var(--typography-secondary-color);

    :first-child {
      margin-right: 7px;
    }
  }

  .active-setting {
    position: relative;

    border-radius: 18px;
    background-color: var(--primary-active-color);

    color: var(--typography-title-color);

    &::before {
      position: absolute;
      left: -13px;

      content: ' ';

      height: 100%;
      width: 3px;

      background-color: var(--primary-color);
    }
  }

  .active-icon {
    color: var(--primary-color);
  }
}
</style>
