<template>
  <MainLayout>
    <router-view></router-view>
  </MainLayout>
</template>

<script>
import MainLayout from '@components/layout/MainLayout'

export default {
  name: 'CreateWorkspaceView',
  components: {
    MainLayout,
  },
}
</script>

<style lang="scss" scoped>
.back-button {
  cursor: pointer;

  color: var(--typography-secondary-color);
  font-size: 14px;
}

.arrow-back {
  margin-right: 6px;
}

.title {
  margin: 5px 0 2px;

  color: var(--typography-primary-color);

  font-size: 36px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.progress-bar-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  border: 1px solid var(--button-primary-color);
  box-shadow: 0 0 3px var(--box-shadow-color);

  color: var(--typography-primary-color);
  background-color: var(--primary-bg-color);
}

.progress-line {
  width: 34px;
  height: 2px;

  background-color: var(--progress-line);
}

.hint {
  color: var(--typography-secondary-color);

  font-size: 14px;
}
</style>
