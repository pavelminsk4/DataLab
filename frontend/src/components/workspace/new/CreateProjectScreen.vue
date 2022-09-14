<template>
  <StepsLayout>
    <template #navigation>
      <StepsNav
        :step="step"
        :title="'Create Project'"
        :hint="'Name the project and choose source Type'"
        :is-not-active-button="!this.projectName"
        @create-project="createProject"
      />
    </template>

    <template #form>
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
            class="description-field"
            placeholder="Some words about your project"
            v-model="description"
          />
        </div>

        <div class="radio-buttons">
          <BaseRadio
            v-for="(item, index) in typesOfSources"
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
  </StepsLayout>
</template>

<script>
import {mapActions} from 'vuex'
import {action} from '@store/constants'

import BaseInput from '@/components/BaseInput'
import BaseSelect from '@/components/BaseSelect'
import BaseRadio from '@/components/BaseRadio'
import BaseButton from '@/components/buttons/BaseButton'

import SocialRadioIcon from '@/components/icons/SocialRadioIcon'
import OnlineRadioIcon from '@/components/icons/OnlineRadioIcon'
import PremiumRadioIcon from '@/components/icons/PremiumRadioIcon'
import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import SelectRadioIcon from '@/components/icons/SelectRadioIcon'
import StepsLayout from '@/components/layout/StepsLayout'
import StepsNav from '@/components/navigation/StepsNav'

export default {
  name: 'CreateProjectScreen',
  components: {
    StepsNav,
    StepsLayout,
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
  computed: {
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
    ...mapActions([action.UPDATE_NEW_WORKSPACE]),
    changeValue(newValue) {
      this.selectedValue = newValue
    },
    createProject() {
      try {
        this[action.UPDATE_NEW_WORKSPACE]({
          projects: [
            {
              title: this.projectName,
              description: this.description,
              source: this.selectedValue.name,
            },
          ],
        })
        this.$router.push({
          name: 'Step3',
        })
      } catch (e) {
        console.log(e)
      }
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
