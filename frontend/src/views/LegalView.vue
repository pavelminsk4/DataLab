<template>
  <MainLayout>
    <section class="header">
      <h1 class="title">{{ title }}</h1>
      <div class="logo">
        <LogoIcon />
      </div>
    </section>
    <router-view></router-view>
  </MainLayout>
</template>

<script>
import MainLayout from '@components/layout/MainLayout'
import LogoIcon from '@components/icons/LogoIcon'

export default {
  name: 'LegalView',
  components: {MainLayout, LogoIcon},
  data() {
    return {
      title: '',
    }
  },
  created() {
    if (this.$route.path.includes('privacy')) {
      this.title = 'Privacy Policy'
    } else {
      this.title = 'Service Agreement & Terms of Use'
    }
  },
}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  gap: 25px;
  height: 190px;

  background-color: var(--background-primary-color);

  .title {
    font-size: 28px;
    line-height: 28px;
  }

  .logo {
    padding: 8px 12px;
    background: var(--neutral-secondary-color);
    border-radius: 16px;
  }
}
</style>
