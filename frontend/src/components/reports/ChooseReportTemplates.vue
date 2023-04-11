<template>
  <div class="wrapper">
    <ReportTemplateCard
      v-for="templateTittle in templateTitles"
      v-model:templateChecked="templates[templateTittle].checked"
      v-model:selectedProjects="templates[templateTittle].selectedProjects"
      :templateTitle="templateTittle"
      :projects="projects"
      :key="templateTittle"
    />
  </div>
</template>

<script>
import ReportTemplateCard from '@/components/reports/ReportTemplateCard.vue'

export default {
  components: {ReportTemplateCard},
  data() {
    return {
      templates: {
        dashboard: {
          checked: true,
          selectedProjects: [],
        },
        summary: {
          checked: false,
          selectedProjects: [],
        },
        sentiment: {
          checked: false,
          selectedProjects: [],
        },
        demography: {
          checked: false,
          selectedProjects: [],
        },
        influencers: {
          checked: true,
          selectedProjects: [],
        },
      },
    }
  },
  created() {
    this.templateTitles = [
      'dashboard',
      'summary',
      'sentiment',
      'demography',
      'influencers',
    ]
    this.projects = ['Saudi Arabia', 'Labor', 'Cyberpunk', 'The Witcher', 'WoW']
    this.templateTitles.map(
      (template) => (this.templates[template].selectedProjects = this.projects)
    )
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  padding-top: 40px;
}
</style>
