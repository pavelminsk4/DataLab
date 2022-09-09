<template>
  <div class="back-button" @click="backToHome">
    <ArrowLeftIcon class="arrow-back" />
    Back
  </div>

  <div class="create-project-title">
    <H1 class="title">The Workspace</H1>
    <div class="progress-bar-wrapper">
      <div class="progress-bar">
        <div class="progress-item">1</div>
        <div class="progress-line"></div>
        <div class="progress-item">2</div>
        <div class="progress-line"></div>
        <div class="progress-item">3</div>
      </div>
      <BaseButton class="next-button" @click="addWorkspace"> Next </BaseButton>
    </div>
  </div>

  <div class="hint">Create a new workspace on your Dashboard</div>

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

<script>
import BaseInput from '@components/BaseInput'
import BaseButton from '@components/buttons/BaseButton'
import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'

export default {
  name: 'CreateWorkspace',
  components: {ArrowLeftIcon, BaseButton, BaseInput},
  component: {
    BaseButton,
    ArrowLeftIcon,
    BaseInput,
  },

  data() {
    return {
      loading: false,
      title: '',
      description: '',
    }
  },
  props: {
    member: {
      type: [Number, String],
      default: '',
    },
  },
  computed: {
    members() {
      let members = []
      members.push(this.member)
      return members
    },
  },
  methods: {
    addWorkspace() {
      this.$emit('create-workspace', this.title, this.description, this.members)
    },
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.back-button {
  cursor: pointer;

  color: var(--secondary-text-color);
}

.arrow-back {
  margin-right: 6px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
}

.progress-bar-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  border: 1px solid var(--primary-button-color);
  box-shadow: 0 0 3px var(--box-shadow-color);

  color: var(--primary-text-color);
  background-color: var(--primary-bg-color);
}

.progress-line {
  width: 34px;
  height: 2px;

  background-color: var(--progress-line);
}

.next-button {
  width: 114px;
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}

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
