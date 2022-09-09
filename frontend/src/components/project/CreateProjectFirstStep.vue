<template>
  <div class="back-button" @click="backToHome">
    <ArrowLeftIcon class="arrow-back" />
    Back
  </div>

  <div class="create-project-title">
    <H1 class="title">Create Project</H1>
    <div class="progress-bar-wrapper">
      <div class="progress-bar">
        <div class="progress-item">1</div>
        <div class="progress-line"></div>
        <div class="progress-item">2</div>
        <div class="progress-line"></div>
        <div class="progress-item">3</div>
      </div>
      <BaseButton class="next-button" @click="nextStep"> Next </BaseButton>
    </div>
  </div>
  <div class="hint">Name the project and choose source Type</div>

  <section class="form-section">
    <div>
      <h4 class="project-name">Name</h4>
      <BaseInput
        class="input-field"
        :placeholder="'Project Name'"
        v-model="nameProject"
      />

      <h4 class="project-name">Workspace</h4>
      <BaseSelect
        v-model="workspace"
        :value="workspace"
        class="select"
        :list="headingsWorkspaces"
        @select-option="selectWorkspace"
      />

      <h4 class="project-name">Description</h4>
      <textarea
        class="description-field"
        placeholder="Some words about your project"
        v-model="description"
      />
    </div>

    <div class="radio-buttons">
      <BaseRadio
        v-for="(item, index) in deliveryChannels"
        :key="index"
        class="radio-button"
        :label="item.name"
        :value="selectedProxy"
        :checked="item"
        :is-background="true"
        v-model="selectedProxy"
        @change="changeValue(item)"
      >
        <template v-slot:default>
          <div class="radio-title">
            {{ item.name }}
            <div class="icon-section">
              <component
                :is="checkSelectOption(selectedProxy.name, item)"
                v-bind="$attrs"
              />
            </div>
          </div>
        </template>

        <template v-slot:description>
          <div class="radio-description">{{ item.description }}</div>
        </template>
      </BaseRadio>
    </div>
  </section>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseInput from '@components/BaseInput'
import BaseSelect from '@components/BaseSelect'
import BaseRadio from '@components/BaseRadio'
import BaseButton from '@components/buttons/BaseButton'

import SocialRadioIcon from '@/components/icons/SocialRadioIcon'
import OnlineRadioIcon from '@/components/icons/OnlineRadioIcon'
import PremiumRadioIcon from '@/components/icons/PremiumRadioIcon'
import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'
import SelectRadioIcon from '@components/icons/SelectRadioIcon'

export default {
  name: 'CreateProjectFirstStep',
  components: {
    BaseInput,
    BaseSelect,
    BaseRadio,
    BaseButton,
    ArrowLeftIcon,
    OnlineRadioIcon,
    PremiumRadioIcon,
    SocialRadioIcon,
    SelectRadioIcon,
  },
  data() {
    return {
      deliveryChannels: [
        {
          name: 'Social',
          description: 'Delivers data from Twitter and Facebook',
          icon: 'Social',
        },
        {
          name: 'Online',
          description: 'Delivers results from Twitter and news',
          icon: 'Online',
        },
        {
          name: 'Premium',
          description: 'Delivers results from Radio and TV',
          icon: 'Premium',
        },
      ],
      nameProject: '',
      description: '',
      selectedValue: {},
      workspace: null,
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
    selectedProxy: {
      get() {
        return this.selectedValue
      },
      set(val) {
        this.selectedValue = val
      },
    },
    headingsWorkspaces() {
      return this.workspaces.map((el) => el.title)
    },
    workspaceId() {
      return this.workspaces.filter((el) => el.title === this.workspace)[0].id
    },
    chanelType() {
      if (this.selectedValue.name === 'Online') {
        return {online: true}
      } else if (this.selectedValue.name === 'Social') {
        return {social: true}
      } else if (this.selectedValue.name === 'Premium') {
        return {premium: true}
      }

      return {}
    },
  },
  async created() {
    await this[action.GET_WORKSPACES]()
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    changeValue(newValue) {
      this.selectedValue = newValue
    },
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },
    nextStep() {
      this.$emit(
        'next-step',
        this.nameProject,
        this.chanelType,
        this.workspaceId
      )
    },
    selectWorkspace(option) {
      this.workspace = option
    },
    checkSelectOption(selectedItem, item) {
      return selectedItem === item.name
        ? 'SelectRadioIcon'
        : item.icon + 'RadioIcon'
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

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
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

.project-name {
  margin: 25px 0 12px;

  font-size: 14px;

  color: var(--primary-text-color);

  &:first-child {
    margin-top: 0;
  }
}

.radio-buttons {
  display: flex;

  margin: 0 -12px 0;
}

.radio-button {
  height: 118px;
  width: 202px;

  margin: 0 12px 0;
}

.form-section {
  display: flex;
  justify-content: space-between;

  margin-top: 40px;
}

.select {
  width: 475px;
}

.input-field {
  width: 475px;
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

.radio-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.radio-description {
  margin-top: 7px;

  font-size: 14px;
  color: var(--secondary-text-color);
}

@media screen and (max-width: 1300px) {
  .form-section {
    flex-direction: column;
  }

  .radio-buttons {
    margin: 30px -15px 30px;
  }
}
</style>

<style>
.input-field > input {
  width: 475px;
}

.selected > .radio-description {
  color: var(--primary-text-color);
}

.icon-section {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 34px;
  width: 34px;

  border: 1px solid #9198a7;
  border-radius: 29px;
}
</style>
