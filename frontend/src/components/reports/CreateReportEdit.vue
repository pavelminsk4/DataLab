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
      v-for="[projectId, project] in projectsWidgetsList"
      :key="projectId"
      :id="projectId"
      class="report-widgets-view"
    >
      <div class="project__header">
        <h3 class="project__title">
          <ReportsProjectIcon /> {{ project.title }}
        </h3>
        <BaseButton @click="addWidget(projectId)">
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
    }
  },
  computed: {
    ...mapState({
      loading: (state) => state.loading,
      newReport: (state) => state.newReport,
      reportWidgetsLists: (state) => state.reportWidgetsLists,
    }),
    projects() {
      return this.newReport.projects
    },
    projectsWidgetsTemplates() {
      return this.newReport.widgetsTemplates
    },
    widgetsList() {
      return {
        online: onlineWidgetsList,
        social: socialWidgetsList,
      }
    },

    widgetsListName() {
      const widgetsNameList = new Map()
      this.projectsWidgetsTemplates.forEach((project, projectId) => {
        const moduleType = project.moduleType.toLowerCase()

        let widgetsListName = []
        console.log('WHAAAAAATTTT', project)
        project.widgetsTemplates.forEach((template) => {
          let templateWidgets = []
          if (template === 'dashboard') {
            templateWidgets = this.getActiveWidgets(
              this.reportWidgetsLists[project.id] || {}
            )
          } else {
            templateWidgets = this.widgetsList[moduleType][template].map(
              (widget) => widget.name
            )
            console.log('-------------------------')
            console.log('template', template)
            console.log('widgetsList[][]', this.widgetsList[moduleType])
            console.log(
              'widgetsList[][]',
              this.widgetsList[moduleType][template]
            )
            console.log('templateWidgets', templateWidgets)
            console.log('-------------------------')
          }
          widgetsListName.push(...templateWidgets)
        })
        widgetsNameList.set(projectId, [...new Set(widgetsListName)])
      })
      console.log('???', widgetsNameList)
      return widgetsNameList
    },

    projectsWidgetsList() {
      const projectsList = new Map()
      this.projects.forEach((project) => {
        const currentWidgetsListName = this.widgetsListName.get(project.id)

        projectsList.set(project.id, {
          ...project,
          widgetsList: this.selectedWidgets(currentWidgetsListName, project.id),
        })
      })

      return projectsList
    },

    newWidgetsLists: {
      get() {
        if (this.newReportWidgetsLists) return this.newReportWidgetsLists

        const newReportWidgetsLists = {
          ...this.reportWidgetsLists,
        }

        this.projects.forEach((project) => {
          const widgetsNames = this.widgetsListName.get(project.id)
          widgetsNames.forEach((widgetName) => {
            newReportWidgetsLists[project.id][widgetName].is_active = true
          })
        })
        return newReportWidgetsLists
      },
      set(val) {
        console.log('TTTTTTT', val)
        this.newReportWidgetsLists = val
      },
    },
  },
  created() {
    this.getWidgetsLists(this.projects)
  },
  methods: {
    ...mapActions({
      getWidgetsLists: action.GET_WIDGETS_LISTS,
      createReport: action.CREATE_REGULAR_REPORT,
    }),
    ...mapActionsSocial({
      getSocialAvailableWidgets: action.GET_AVAILABLE_WIDGETS,
    }),
    async saveReport() {
      const items = this.projectsWidgetsList.map((project) => {
        const isSocial = project.moduleType === 'Social'
        const prefix = isSocial ? 'soc_' : 'onl_'
        const widgetsObj = {}

        Object.keys(this.reportWidgetsLists[project.id]).forEach(
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

      const newWidgetsNameList = this.getActiveWidgets(widgetsList)
      const newWidgetsList = this.selectedWidgets(newWidgetsNameList)
      const currentProject = this.projectsWidgetsList.get(projectId)
      this.projectsWidgetsList.set(projectId, {
        ...currentProject,
        widgetsList: newWidgetsList,
      })
      console.log(this.projectsWidgetsList)
    },

    getActiveWidgets(widgetsList) {
      return Object.keys(widgetsList).filter(
        (widgetName) => widgetsList[widgetName].is_active
      )
    },
    selectedWidgets(widgetsList, projectId) {
      if (!this.reportWidgetsLists[projectId]) return
      return widgetsList.map((widgetName) => {
        if (this.reportWidgetsLists[projectId][widgetName]) {
          return {
            name: widgetName,
            isFullWidth: true,
            widgetDetails: getWidgetDetails(
              widgetName,
              this.reportWidgetsLists[projectId][widgetName],
              projectId
            ),
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
