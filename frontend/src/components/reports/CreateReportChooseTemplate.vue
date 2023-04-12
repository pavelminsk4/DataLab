<template>
  <div v-if="projects.length" class="wrapper">
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
import {mapState} from 'vuex'

import ReportTemplateCard from '@/components/reports/ReportTemplateCard.vue'

export default {
  name: 'CreateReportChooseTemplate',
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
  computed: {
    ...mapState(['newReport']),
    projects() {
      return this.newReport.projects
    },
  },
  created() {
    this.templateTitles = [
      'dashboard',
      'summary',
      'sentiment',
      'demography',
      'influencers',
    ]

    this.templateTitles.forEach((template) =>
      this.projects.forEach((project) =>
        this.templates[template].selectedProjects.push(project.id)
      )
    )
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
}
</style>
