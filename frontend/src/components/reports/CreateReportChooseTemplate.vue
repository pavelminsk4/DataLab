<template>
  <div v-if="projects.length" class="wrapper">
    <ReportTemplateCard
      v-for="templateName in templatesNames"
      v-model:templateChecked="widgetsTemplates[templateName].checked"
      v-model:selectedProjects="widgetsTemplates[templateName].selectedProjects"
      :template-name="templateName"
      :template-title="widgetsTemplates[templateName].title"
      :projects="projects"
      :key="templateName"
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
import {mapState} from 'vuex'
import createReportMixin from '@/lib/mixins/create-report.js'

import ReportTemplateCard from '@/components/reports/ReportTemplateCard'

export default {
  name: 'CreateReportChooseTemplate',
  mixins: [createReportMixin],
  components: {ReportTemplateCard},
  data() {
    return {
      widgetsTemplates: {
        dashboard: {
          title: 'analytics',
          checked: false,
          selectedProjects: [],
        },
        summary: {
          title: 'summary',
          checked: false,
          selectedProjects: [],
        },
        sentiment: {
          title: 'sentiment',
          checked: false,
          selectedProjects: [],
        },
        demography: {
          title: 'demography',
          checked: false,
          selectedProjects: [],
        },
        influencers: {
          title: 'influencers',
          checked: false,
          selectedProjects: [],
        },
      },
    }
  },
  computed: {
    ...mapState(['templates']),
    projects() {
      return this.newReport.projects
    },
    templatesNames() {
      return Object.keys(this.widgetsTemplates)
    },
    selectedWidgetsTemplates() {
      const selectedTemplates = {}
      this.templatesNames.forEach((templateName) => {
        if (this.widgetsTemplates[templateName].checked) {
          selectedTemplates[templateName] = this.widgetsTemplates[templateName]
        }
      })
      return selectedTemplates
    },
  },
  created() {
    this.templatesNames.forEach(
      (template) =>
        (this.widgetsTemplates[template].selectedProjects = this.projects)
    )
  },
  methods: {
    nextStep() {
      const nextStep = 5
      const nextStepName = this.getNextStepName(nextStep)

      const projectsWithTemplates = this.getProjectsWithTemplates()

      const reportData = {
        step: nextStep,
        widgetsTemplates: projectsWithTemplates,
      }

      if (!this.newReport.report_template) {
        reportData.report_template = this.templates[0]?.id || ''
      }

      this[action.UPDATE_NEW_REPORT](reportData)
      this.$router.push({name: nextStepName})
    },
    getProjectsWithTemplates() {
      const projectsWithTemplates = new Map()
      this.projects.forEach((project) => {
        const templates = Object.keys(this.selectedWidgetsTemplates).filter(
          (templateName) =>
            this.widgetsTemplates[templateName].selectedProjects.find(
              (selectProject) => {
                return selectProject.id === project.id
              }
            )
        )

        projectsWithTemplates.set(project.id, {
          ...project,
          widgetsTemplates: templates,
        })
      })

      return projectsWithTemplates
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
