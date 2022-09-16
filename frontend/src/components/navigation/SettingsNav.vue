<template>
  <div class="settings-nav-wrapper">
    <div v-for="(item, index) in settings" :key="'setting' + index">
      <div class="nav-title">{{ item.name }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingsNav',
  data() {
    return {
      settings: [
        {
          name: 'Analytics',
        },
        {
          name: 'Search',
        },
        {
          name: 'Alerts',
        },
        {
          name: 'Reports',
        },
        {
          name: 'Settings',
        },
      ],
    }
  },
}
</script>

<style scoped>
.settings-nav-wrapper {
  position: absolute;
  left: 0;

  display: flex;
  align-items: center;

  width: 100%;
  height: 50px;
  padding: 0 69px 0 79px;

  background-color: var(--primary-button-color);
}

.nav-title {
  margin-right: 34px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;

  color: #ffffff;
}
</style>
