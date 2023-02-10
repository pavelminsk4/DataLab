<template>
  <NavigationBar
    v-if="currentStep === 'Step2'"
    :step="step"
    title="Create Project"
    hint="Name the project and choose source Type"
    :is-active-button="!!projectName && !!selectedValue.name"
    @next-step="nextStep"
  />

  <NavigationBar
    v-else
    :step="step"
    title="Create Project"
    hint="Name the project and choose source Type"
    :is-existing-workspace="true"
    :is-active-button="!!projectName && !!selectedValue.name"
    @next-step="nextStepForExistingWorkspace"
  />

  <section class="form-section">
    <div>
      <h4 class="project-name">Name</h4>
      <BaseInput
        class="input-field"
        :placeholder="'Project Name'"
        v-model="projectName"
      />

      <h4 class="project-name">Description</h4>
      <textarea
        class="description-field scroll"
        placeholder="Some words about your project"
        v-model="description"
      />
    </div>

    <div class="radio-buttons">
      <SourceTypeCard
        v-for="(item, index) in typesOfSources"
        :key="index"
        class="radio-button"
        :label="item.name"
        :value="selectedProxy"
        :checked="item"
        :is-background="true"
        :is-disabled="item.name !== 'Online'"
        @change="changeValue(item)"
      >
        <template #default>
          <div class="radio-title">
            {{ item.name }}
            <div class="icon-section">
              <component :is="checkSelectOption(selectedProxy.name, item)" />
            </div>
          </div>
        </template>

        <template #description>
          <div class="radio-description">{{ item.description }}</div>
        </template>
      </SourceTypeCard>
    </div>
  </section>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import BaseInput from '@/components/BaseInput'
import BaseSelect from '@/components/BaseSelect'
import BaseButton from '@/components/buttons/BaseButton'

import NavigationBar from '@/components/navigation/NavigationBar'

import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import SelectRadioIcon from '@/components/icons/SelectRadioIcon'
import SocialRadioIcon from '@/components/icons/SocialRadioIcon'
import OnlineRadioIcon from '@/components/icons/OnlineIcon'
import PremiumRadioIcon from '@/components/icons/PremiumRadioIcon'
import SourceTypeCard from '@/components/SourceTypeCard'

export default {
  name: 'CreateProjectScreen',
  components: {
    SourceTypeCard,
    NavigationBar,
    BaseInput,
    BaseSelect,
    BaseButton,
    ArrowLeftIcon,
    OnlineRadioIcon,
    PremiumRadioIcon,
    SocialRadioIcon,
    SelectRadioIcon,
  },
  data() {
    return {
      typesOfSources: [
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
      projectName: '',
      description: '',
      selectedValue: {},
    }
  },
  created() {
    if (this.step === 'ProjectStep1') this[action.CLEAR_STATE]()
  },
  computed: {
    ...mapState(['currentStep', 'userInfo']),
    step() {
      return this.$route.name
    },
    selectedProxy: {
      get() {
        return this.selectedValue
      },
      set(val) {
        this.selectedValue = val
      },
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_PROJECT_STATE,
      action.UPDATE_CURRENT_STEP,
      action.CLEAR_STATE,
    ]),
    changeValue(newValue) {
      this.selectedValue = newValue
    },
    checkSelectOption(selectedItem, item) {
      return selectedItem === item.name
        ? 'SelectRadioIcon'
        : item.icon + 'RadioIcon'
    },
    nextStep() {
      try {
        this[action.UPDATE_CURRENT_STEP]('Step3')
        this[action.UPDATE_PROJECT_STATE]({
          creator: this.userInfo.id,
          title: this.projectName,
          description: this.description,
          source: this.selectedValue.name,
        })
        this.$router.push({
          name: 'Step3',
        })
      } catch (e) {
        console.log(e)
      }
    },
    nextStepForExistingWorkspace() {
      try {
        this[action.UPDATE_CURRENT_STEP]('ProjectStep2')
        this[action.UPDATE_PROJECT_STATE]({
          creator: this.userInfo.id,
          title: this.projectName,
          description: this.description,
          source: this.selectedValue.name,
          workspace: this.$route.params.workspaceId,
        })
        this.$router.push({
          name: 'ProjectStep2',
        })
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.project-name {
  margin: 25px 0 12px;

  font-size: 14px;

  color: var(--typography-primary-color);

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

  color: var(--typography-primary-color);

  resize: none;
}

.description-field::placeholder {
  color: var(--typography-secondary-color);
}

.radio-title {
  display: flex;
  justify-content: space-between;
  align-items: center;

  color: var(--typography-primary-color);
}

.radio-description {
  margin-top: 7px;

  font-size: 14px;
  color: var(--typography-secondary-color);
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
  color: var(--typography-primary-color);
}

.icon-section {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 34px;
  width: 34px;

  border: 1px solid #9198a7;
  border-radius: 29px;

  color: var(--typography-primary-color);
}
</style>
