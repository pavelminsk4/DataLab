<template>
  <div v-if="projects.length" class="wrapper">
    <ReportTemplateCard
      v-for="templateTittle in templateTitles"
      v-model:templateChecked="widgetsTemplates[templateTittle].checked"
      v-model:selectedProjects="
        widgetsTemplates[templateTittle].selectedProjects
      "
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
    ...mapState(['templates']),
    projects() {
      return this.newReport.projects
    },
    templateTitles() {
      return Object.keys(this.widgetsTemplates)
    },
    selectedWidgetsTemplates() {
      const selectedTemplates = {}
      this.templateTitles.forEach((templateName) => {
        if (this.widgetsTemplates[templateName].checked) {
          selectedTemplates[templateName] = this.widgetsTemplates[templateName]
        }
      })
      return selectedTemplates
    },
  },
  created() {
    this.templateTitles.forEach(
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
        reportData.report_template = this.templates[0].id
      }

      this[action.UPDATE_NEW_REPORT](reportData)
      this.$router.push({name: nextStepName})
    },
    getProjectsWithTemplates() {
      const projectsWithTemplates = new Map()
      this.projects.forEach((project) => {
        const templates = this.templateTitles.filter((templateName) =>
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
