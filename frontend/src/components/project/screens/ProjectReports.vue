<template>
  <ProjectSettingsLayout>
    <ProjectNav />
  </ProjectSettingsLayout>
</template>

<script>
import ProjectNav from '@/components/navigation/ProjectNav'
import ProjectSettingsLayout from '@/components/layout/ProjectSettingsLayout'

export default {
  name: 'ProjectReports',
  components: {ProjectNav, ProjectSettingsLayout},
}
</script>

<style scoped>
.project-nav {
  margin-top: 30px;
}
</style>
