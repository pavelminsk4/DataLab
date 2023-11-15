<template>
  <BaseTable
    :table-header="tableHeader"
    :has-actions="false"
    :has-select-all="hasSelectAll"
    class="project-table"
    @select-all="selectAll"
  >
    <template v-if="workspaces.length">
      <template
        v-for="{id: workspaceId, title, projects, members} in workspaces"
        :key="workspaceId"
      >
        <tr
          :id="workspaceId"
          @click="
            this.isOpenWorkspace[workspaceId] =
              !this.isOpenWorkspace[workspaceId]
          "
          :class="[
            'workspace-row',
            this.isOpenWorkspace[workspaceId] && 'open-workspace',
            isSelectedWorkspace(projects) && 'selected',
          ]"
        >
          <td class="workspace-icon">
            <ArrowheadIcon
              :direction="this.isOpenWorkspace[workspaceId] ? 'top' : 'down'"
            />
          </td>
          <td class="workspace-title">{{ title }}</td>
          <td>
            <div class="chips-height">
              <BaseChips :chips-type="projects[0].source" />
            </div>
          </td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>

        <template v-if="this.isOpenWorkspace[workspaceId]">
          <tr
            v-for="(project, index) in projects"
            :key="project.id"
            :id="project.id"
            :class="[
              'project-row',
              index + 1 === projects.length && 'project-last-row',
              isSelected(project.id) && 'selected',
            ]"
          >
            <td>
              <BaseCheckbox
                v-model="selectedProjects"
                :value="{
                  id: project.id,
                  title: project.title,
                  moduleType: project.source,
                }"
              />
            </td>
            <td>{{ project.title }}</td>
            <td>
              <div class="chips-height">
                <BaseChips :chips-type="project.source" />
              </div>
            </td>
            <td>
              <TagsCollapsible
                v-if="project.keywords.length"
                :tags="project.keywords"
              />
            </td>
            <td>
              <UsersIconsBar :users="project.members" />
            </td>
            <td>
              <div class="creator">
                <UserAvatar
                  :avatar-url="
                    currentMember(members, project.creator)?.user_profile.photo
                  "
                  :first-name="
                    currentMember(members, project.creator)?.first_name
                  "
                  :last-name="
                    currentMember(members, project.creator)?.last_name
                  "
                  :username="currentMember(members, project.creator)?.username"
                />
                <div>
                  {{ currentMember(members, project.creator)?.username }}
                </div>
              </div>
            </td>
            <td class="project-creation-date">
              {{ creationDate(project.created_at) }}
            </td>
          </tr>
        </template>
      </template>
    </template>
  </BaseTable>
</template>

<script>
import TagsCollapsible from '@components/TagsCollapsible'
import BaseTable from '@components/common/BaseTable'
import BaseCheckbox from '@components/BaseCheckbox2'
import BaseChips from '@components/BaseChips'
import UserAvatar from '@components/UserAvatar'
import UsersIconsBar from '@components/UsersIconsBar'

import ArrowheadIcon from '@components/icons/ArrowheadIcon'

export default {
  name: 'WorkspaceTableWithProjects',
  components: {
    ArrowheadIcon,
    BaseCheckbox,
    BaseChips,
    BaseTable,
    TagsCollapsible,
    UserAvatar,
    UsersIconsBar,
  },
  props: {
    modelValue: {type: Array, required: true},
    projects: {type: Array, required: true},
    workspaces: {type: Array, required: true},
    hasSelectAll: {type: Boolean, default: true},
  },
  data() {
    return {
      isOpenWorkspace: {},
    }
  },
  computed: {
    selectedProjects: {
      get() {
        return this.modelValue
      },
      set(val) {
        this.$emit('update:modelValue', val)
      },
    },
  },
  created() {
    this.tableHeader = [
      {name: 'project name', width: ''},
      {name: 'type', width: '15%'},
      {name: 'keywords', width: '20%'},
      {name: 'assigned user', width: '11%'},
      {name: 'creator', width: '16%'},
      {name: 'date', width: '11%'},
    ]
  },
  methods: {
    currentMember(members, id) {
      return members.find((el) => el.id === id)
    },
    creationDate(date) {
      return new Date(date).toLocaleDateString('ro-RO')
    },
    selectAll(isSelectAll) {
      this.selectedProjects = isSelectAll
        ? this.projects.map((value) => {
            return {
              id: value.id,
              title: value.title,
              moduleType: value.source,
            }
          })
        : []
    },
    isSelected(projectId) {
      return this.selectedProjects.find((project) => project.id === projectId)
    },
    isSelectedWorkspace(projects) {
      return projects.find((project) =>
        this.selectedProjects.find(
          (selectedProject) => selectedProject.id === project.id
        )
      )
    },
  },
}
</script>

<style lang="scss">
.project-table {
  --border-lines-block: 2px solid #b1b6bb;

  .workspace-icon {
    vertical-align: middle;
    text-align: center;
  }

  .workspace-title {
    font-weight: 600;
    font-size: 14px;
  }

  .selected {
    background-color: var(--primary-active-color);
  }

  .project-row {
    td {
      &:first-child {
        border-left: var(--border-lines-block);
      }

      &:last-child {
        border-right: var(--border-lines-block);
      }
    }
  }

  .project-last-row {
    td {
      border-bottom: var(--border-lines-block);
    }
  }

  .open-workspace {
    td {
      border-top: var(--border-lines-block);
      border-bottom: var(--border-lines-block);

      &:first-child {
        border-left: var(--border-lines-block);
      }

      &:last-child {
        border-right: var(--border-lines-block);
      }
    }
  }
}

tr {
  position: relative;
  td {
    vertical-align: initial;
  }

  &:not(:last-child) {
    td {
      border-bottom: var(--border-primary);
    }
  }
}

.creator {
  display: flex;
  align-items: center;
}
</style>
