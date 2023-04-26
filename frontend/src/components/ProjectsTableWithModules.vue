<template>
  <BaseTable
    :table-header="tableHeader"
    :has-actions="false"
    @select-all="selectAll"
  >
    <template v-if="projects.length">
      <tr
        v-for="(project, index) in projects"
        :key="index"
        :id="project.id"
        :class="('project-row', isSelected(project.id) && 'selected')"
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
          <div class="creator">
            <!-- <UserAvatar
              :avatar-url="currentMember(project.creator)?.user_profile.photo"
              :first-name="currentMember(project.creator)?.first_name"
              :last-name="currentMember(project.creator)?.last_name"
              :username="currentMember(project.creator)?.username"
            />
            <div>{{ currentMember(project.creator).username }}</div> -->
          </div>
        </td>
        <td>
          <!-- <UsersIconsBar :users="projectMembers(project.members)" /> -->
        </td>
        <td class="project-creation-date">
          {{ projectCreationDate(project.created_at) }}
        </td>

        <div class="divider"></div>
      </tr>
    </template>
  </BaseTable>
</template>

<script>
import TagsCollapsible from '@components/TagsCollapsible'
import BaseTable from '@components/common/BaseTable'
import BaseCheckbox from '@/components/BaseCheckbox2'
import BaseChips from '@/components/BaseChips'

export default {
  components: {TagsCollapsible, BaseTable, BaseCheckbox, BaseChips},
  props: {
    modelValue: {type: Array, required: true},
    projects: {type: Array, required: true},
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
      {name: 'type', width: '14%'},
      {name: 'keywords', width: '20%'},
      {name: 'assigned user', width: '11%'},
      {name: 'creator', width: '16%'},
      {name: 'date', width: '11%'},
    ]
  },
  methods: {
    projectMembers(projectMembersIds) {
      return projectMembersIds.length
    },
    projectCreationDate(date) {
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
  },
}
</script>

<style lang="scss">
.wrapper {
  height: 50vh;
  .selected {
    background-color: var(--primary-active-color);
  }
}
</style>
