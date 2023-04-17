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

  <footer class="create-reports__footer">
    <ButtonWithArrow @click="nextStep">
      <span>Next</span>
    </ButtonWithArrow>
  </footer>
</template>

<script>
import {action} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'

import ReportTemplateCard from '@/components/reports/ReportTemplateCard'

export default {
  name: 'CreateReportChooseTemplate',
  mixins: [createReportMixin],
  components: {ReportTemplateCard},
  data() {
    return {
      templates: {
        dashboard: {
          checked: false,
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
          checked: false,
          selectedProjects: [],
        },
      },
    }
  },
  computed: {
    projects() {
      return this.newReport.projects
    },
    templateTitles() {
      return Object.keys(this.templates)
    },
  },
  created() {
    this.templateTitles.forEach(
      (template) => (this.templates[template].selectedProjects = this.projects)
    )
  },
  methods: {
    nextStep() {
      const nextStep = 5
      const nextStepName = this.getNextStepName(nextStep)

      const selectedTemplates = {}
      this.templateTitles.forEach((templateName) => {
        if (this.templates[templateName].checked) {
          selectedTemplates[templateName] = this.templates[templateName]
        }
      })

      this[action.UPDATE_NEW_REPORT]({
        step: nextStep,
        templates: selectedTemplates,
      })
      this.$router.push({name: nextStepName})
    },
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
