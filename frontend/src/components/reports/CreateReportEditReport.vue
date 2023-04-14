<template>
  <div class="add-widgets-button">
    <BaseButton @click="saveReport">
      <AddWidgetsIcon />
      <span>Add widgets</span>
    </BaseButton>
  </div>

  <div class="report-projects-view">
    <div
      v-for="project in reportProjects"
      :key="project.id"
      class="report-widgets-view"
    >
      <h3 class="project-title">{{ project.title }}</h3>

      <div class="report-widgets-list">
        <!-- <WidgetsList /> -->
      </div>
    </div>
  </div>
  {{ reportProjects }}
  <footer class="create-reports__footer">
    <BaseButton @click="saveReport">
      <SaveIcon />
      <span>Save Report</span>
    </BaseButton>
  </footer>
</template>

<script>
import {mapState, mapActions, createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import {onlineWidgetsList, socialWidgetsList} from '@/lib/constants'

import AddWidgetsIcon from '@/components/icons/AddWidgetsIcon'
import SaveIcon from '@/components/icons/SaveIcon'

import BaseButton from '@/components/common/BaseButton'
// import WidgetsList from '@/components/widgets/WidgetsList'

const {mapActions: mapActionsSocial} = createNamespacedHelpers('social')

export default {
  name: 'CreateReportEditReport',
  components: {AddWidgetsIcon, BaseButton, SaveIcon},
  computed: {
    ...mapState({
      newReport: (state) => state.newReport,
      onlineAvailableWidgets: (state) => state.availableWidgets,
      socialAvailableWidgets: (state) => state.social.availableWidgets,
    }),
    projects() {
      return this.newReport.projects
    },
    templates() {
      return this.newReport.templates
    },
    widgetsList() {
      return {
        online: onlineWidgetsList,
        social: socialWidgetsList,
      }
    },

    projectsWithTemplates() {
      const projectsData = {}

      Object.keys(this.templates).forEach((templateName) => {
        this.templates[templateName].selectedProjects.forEach((project) => {
          const currentTemplates = projectsData[project.id]?.templates || []
          projectsData[project.id] = {
            ...project,
            templates: [...currentTemplates, templateName],
          }
        })
      })

      return Object.values(projectsData)
    },
    onlineDashboardWidgets() {
      if (!this.onlineAvailableWidgets) return []
      const dashboardWidgetsName = Object.keys(
        this.onlineAvailableWidgets
      ).filter(
        (widgetName) => this.onlineAvailableWidgets[widgetName].is_active
      )
      return dashboardWidgetsName.map((widgetName) => ({name: widgetName}))
    },
    socialDashboardWidgets() {
      if (!this.socialAvailableWidgets) return []
      const dashboardWidgetsName = Object.keys(
        this.socialAvailableWidgets
      ).filter(
        (widgetName) => this.socialAvailableWidgets[widgetName].is_active
      )
      return dashboardWidgetsName.map((widgetName) => ({name: widgetName}))
    },

    reportProjects() {
      const projectsWithWidgets = this.projectsWithTemplates.map((project) => {
        const moduleType = project.moduleType.toLowerCase()

        let widgetsList = []
        project.templates.forEach((template) => {
          let templateWidgets = []
          if (template === 'dashboard') {
            templateWidgets = this[`${moduleType}DashboardWidgets`]
          } else {
            templateWidgets = this.widgetsList[moduleType][template]
          }
          widgetsList.push(...templateWidgets)
        })

        widgetsList = [...new Set(widgetsList)]

        return {
          ...project,
          widgetsList,
        }
      })

      return projectsWithWidgets
    },
  },
  created() {
    const onlineProject = this.projects.find(
      (project) => project.moduleType === 'Online'
    )
    const socialProject = this.projects.find(
      (project) => project.moduleType === 'Social'
    )

    if (onlineProject) {
      this.getOnlineAvailableWidgets(onlineProject.id)
    }
    if (socialProject) {
      this.getSocialAvailableWidgets(socialProject.id)
    }
  },
  methods: {
    ...mapActions({
      getOnlineAvailableWidgets: action.GET_AVAILABLE_WIDGETS,
    }),
    ...mapActionsSocial({
      getSocialAvailableWidgets: action.GET_AVAILABLE_WIDGETS,
    }),
    saveReport() {
      this.$router.push({name: ''})

      console.log()
    },
  },
}
</script>

<style lang="scss" scoped>
.add-widgets-button {
  display: flex;
  justify-content: flex-end;
}

.report-projects-view {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
  padding: 32px;
  margin-top: 20px;

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: var(--border-radius);
}

.report-widgets-view {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;

  &:not(:last-child) {
    margin-bottom: 30px;
  }
}

.project-title {
  align-self: flex-start;
}
</style>
