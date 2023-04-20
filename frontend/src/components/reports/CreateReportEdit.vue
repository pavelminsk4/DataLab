<template>
  <WidgetsListModal
    v-if="isOpenWidgetsModal"
    :project-id="currentProjectId"
    :widgetList="newWidgetsLists[currentProjectId]"
    @close="isOpenWidgetsModal = false"
    @update-available-widgets="updateAvailableWidgets"
  />

  <ul class="report-projects-view">
    <li
      v-for="project in reportProjects"
      :key="project.id"
      :id="project.id"
      class="report-widgets-view"
    >
      <div class="project__header">
        <h3 class="project__title">
          <ReportsProjectIcon /> {{ project.title }}
        </h3>
        <BaseButton @click="addWidget(project.id)">
          <AddWidgetsIcon />
          <span>Add widgets</span>
        </BaseButton>
      </div>

      <div v-if="project.widgetsList" class="report-widgets-list">
        <WidgetsList
          :module-name="project.moduleType"
          :selected-widgets="project.widgetsList"
          :current-project="project"
        />
      </div>
    </li>
  </ul>
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
import {getWidgetDetails} from '@lib/utilities'

import AddWidgetsIcon from '@/components/icons/AddWidgetsIcon'
import SaveIcon from '@/components/icons/SaveIcon'
import ReportsProjectIcon from '@/components/icons/ReportsProjectIcon'

import BaseButton from '@/components/common/BaseButton'
import WidgetsList from '@/components/widgets/WidgetsList'
import WidgetsListModal from '@/components/widgets/modals/WidgetsListModal'

const {mapActions: mapActionsSocial} = createNamespacedHelpers('social')

export default {
  name: 'CreateReportEdit',
  components: {
    AddWidgetsIcon,
    BaseButton,
    SaveIcon,
    ReportsProjectIcon,
    WidgetsList,
    WidgetsListModal,
  },
  data() {
    return {
      isOpenWidgetsModal: false,
      currentProjectId: 0,
      newReportWidgetsLists: null,
      widgetsName: {},
    }
  },
  computed: {
    ...mapState({
      loading: (state) => state.loading,
      newReport: (state) => state.newReport,
      onlineAvailableWidgets: (state) => state.availableWidgets,
      socialAvailableWidgets: (state) => state.social.availableWidgets,
      reportWidgetsList: (state) => state.reportWidgetsList,
    }),
    projects() {
      return this.newReport.projects
    },
    widgetsTemplates() {
      return this.newReport.widgetsTemplates
    },
    widgetsList() {
      return {
        online: onlineWidgetsList,
        social: socialWidgetsList,
      }
    },

    projectsWithTemplates() {
      const projectsWithTemplates = this.projects.map((project) => {
        const templates = Object.keys(this.widgetsTemplates).filter(
          (templateName) =>
            this.widgetsTemplates[templateName].selectedProjects.find(
              (selectProject) => {
                return selectProject.id === project.id
              }
            )
        )
        return {
          ...project,
          widgetsTemplates: templates,
        }
      })

      return projectsWithTemplates
    },

    reportProjects() {
      const projectsWithWidgets = this.projectsWithTemplates.map((project) => {
        const moduleType = project.moduleType.toLowerCase()

        let widgetsList = []
        project.widgetsTemplates.forEach((template) => {
          let templateWidgets = []
          if (template === 'dashboard') {
            templateWidgets = this.getDashboardWidgets(
              this.reportWidgetsList[project.id] || {}
            )
          } else {
            templateWidgets = this.widgetsList[moduleType][template]
          }
          widgetsList.push(...templateWidgets)
        })

        widgetsList = [...new Set(widgetsList)]
        // TODO: temp
        this.widgetsName[project.id] = [
          ...new Set(widgetsList.map((w) => w.name)),
        ]
        // -----
        widgetsList = this.selectedWidgets(widgetsList, project.id)
        return {
          ...project,
          widgetsList,
        }
      })
      return projectsWithWidgets
    },

    newWidgetsLists: {
      get() {
        if (this.newReportWidgetsLists) return this.newReportWidgetsLists

        const newReportWidgetsLists = {
          ...this.reportWidgetsList,
        }

        this.projects.forEach((project) => {
          const widgetsNames = this.widgetsName[project.id]
          widgetsNames.forEach((widgetName) => {
            newReportWidgetsLists[project.id][widgetName].is_active = true
          })
        })

        return newReportWidgetsLists
      },
      set(val) {
        this.newReportWidgetsLists = val
      },
    },
  },
  created() {
    this.getWidgetsList(this.projects)
  },
  methods: {
    ...mapActions({
      getOnlineAvailableWidgets: action.GET_AVAILABLE_WIDGETS,
      getWidgetsList: action.GET_WIDGETS_LISTS,
      createReport: action.CREATE_REGULAR_REPORT,
    }),
    ...mapActionsSocial({
      getSocialAvailableWidgets: action.GET_AVAILABLE_WIDGETS,
    }),
    async saveReport() {
      const items = this.reportProjects.map((project) => {
        const isSocial = project.moduleType === 'Social'
        const prefix = isSocial ? 'soc_' : 'onl_'
        const widgetsObj = {}

        Object.keys(this.reportWidgetsList[project.id]).forEach(
          (widgetName) => {
            widgetsObj[prefix + widgetName] = false
          }
        )

        project.widgetsList.forEach((widget) => {
          widgetsObj[prefix + widget.widgetDetails.name] = true
        })

        return {
          module_type: isSocial ? 'ProjectSocial' : 'Project',
          module_project_id: project.id,
          ...widgetsObj,
        }
      })

      this.createReport({
        departmentId: this.newReport.department,
        data: {
          ...this.newReport,
          items,
        },
      })
      this.$router.push({name: 'Reports'})
    },
    addWidget(projectId) {
      this.isOpenWidgetsModal = true
      this.currentProjectId = projectId
    },
    updateAvailableWidgets({projectId, widgetsList}) {
      this.newWidgetsLists = {
        ...this.newWidgetsLists,
        [projectId]: widgetsList,
      }
      // TODO: fix select widgets
      const index = this.reportProjects.findIndex(
        (project) => project.id === projectId
      )

      this.reportProjects[index].widgetsList.push()
    },

    getDashboardWidgets(widgetsList) {
      return Object.keys(widgetsList)
        .filter((widgetName) => widgetsList[widgetName].is_active)
        .map((widgetName) => ({name: widgetName}))
    },
    selectedWidgets(widgetsList, projectId) {
      if (!this.reportWidgetsList[projectId]) return
      return widgetsList.map((widget) => {
        if (this.reportWidgetsList[projectId][widget.name]) {
          return {
            widgetDetails: getWidgetDetails(
              widget.name,
              this.reportWidgetsList[projectId][widget.name],
              projectId
            ),
            isFullWidth: true,
          }
        }
      })
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

  width: 100%;
  padding: 15px 0px;
}

.report-widgets-view {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
  padding: 35px;

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: var(--border-radius);

  &:not(:last-child) {
    margin-bottom: 30px;
  }
}

.report-widgets-list {
  width: 70%;
}

.project {
  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    width: 100%;
    margin-bottom: 10px;
  }

  &__title {
    display: flex;
    align-items: center;

    svg {
      margin-right: 8px;
    }
  }
}
</style>
