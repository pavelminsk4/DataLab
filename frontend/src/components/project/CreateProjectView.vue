<template>
  <MainLayout>
    <router-view></router-view>
  </MainLayout>
</template>

<script>
import MainLayout from '@/components/layout/MainLayout'
export default {
  name: 'CreateProjectView',
  components: {MainLayout},
}
</script>
