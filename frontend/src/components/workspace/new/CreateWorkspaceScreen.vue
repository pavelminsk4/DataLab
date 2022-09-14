<template>
  <StepsLayout>
    <template #navigation>
      <StepsNav
        :step="step"
        :title="'The Workspace'"
        :hint="'Create a new workspace on your Dashboard'"
        :is-not-active-button="!this.title"
        @next-step="nextStep"
      />
    </template>

    <template #form>
      <div class="workspace-wrapper">
        <h4 class="project-name">Name</h4>
        <BaseInput v-model="title" class="input-field" />

        <h4 class="project-name">Description</h4>
        <textarea
          class="description-field"
          v-model="description"
          placeholder="Some words about Workspace"
        />
      </div>
    </template>
  </StepsLayout>
</template>

<script>
import {mapActions} from 'vuex'
import {action} from '@store/constants'

import BaseInput from '@components/BaseInput'
import StepsNav from '@components/navigation/StepsNav'
import StepsLayout from '@components/layout/StepsLayout'

export default {
  name: 'CreateWorkspaceScreen',
  components: {StepsNav, BaseInput, StepsLayout},
  component: {
    BaseInput,
  },
  props: {
    member: {
      type: [Number, String],
      default: '1',
    },
  },

  data() {
    return {
      title: '',
      description: '',
    }
  },
  computed: {
    step() {
      return this.$route.name
    },
    members() {
      let members = []
      members.push(this.member)
      return members
    },
  },
  methods: {
    ...mapActions([action.UPDATE_NEW_WORKSPACE]),
    async nextStep() {
      try {
        this[action.UPDATE_NEW_WORKSPACE]({
          title: this.title,
          description: this.description,
          members: this.members,
        })
        this.$router.push({
          name: 'Step2',
        })
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.workspace-wrapper {
  display: flex;
  flex-direction: column;

  margin-top: 40px;
}

.project-name {
  margin: 25px 0 12px;

  font-size: 14px;

  color: var(--primary-text-color);

  &:first-child {
    margin-top: 0;
  }
}

.description-field {
  width: 475px;
  height: 132px;
  padding: 12px 16px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);

  resize: none;
}

.description-field::placeholder {
  color: var(--secondary-text-color);
}

.description-field::-webkit-scrollbar {
  width: 10px;
}

.description-field::-webkit-scrollbar-track {
  border-radius: 10px;

  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

.description-field::-webkit-scrollbar-thumb {
  width: 8px;

  border-radius: 10px;

  background-color: var(--box-shadow-color);
  outline: none;
}
</style>
