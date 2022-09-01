<template>
  <section class="form-section">
    <div>
      <h4 class="project-name">Name</h4>
      <BaseInput class="input-field" :placeholder="'Project Name'" />

      <h4 class="project-name">Workspace</h4>
      <BaseSelect
        v-model="workspace"
        class="select"
        :list="headingsWorkspaces"
        @click="test()"
      />

      <h4 class="project-name">Description</h4>
      <textarea
        class="description-field"
        placeholder="Some words about your project"
      />
    </div>

    <div class="radio-buttons">
      <BaseRadio
        v-for="(item, index) in deliveryChannels"
        :key="index"
        class="radio-button"
        :label="item.name"
        :value="selectedValue"
        :checked="item"
        @change="changeValue(item)"
      >
        <template v-slot:default>
          <div class="radio-title">
            {{ item.name }}
            <component :is="item.icon + 'RadioButton'" v-bind="$attrs" />
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
import SocialRadioButton from '@components/icons/SocialRadioButton'
import OnlineRadioButton from '@components/icons/OnlineRadioButton'
import PremiumRadioButton from '@components/icons/PremiumRadioButton'

export default {
  name: 'CreateProjectFirstStep',
  components: {
    BaseInput,
    BaseSelect,
    BaseRadio,
    OnlineRadioButton,
    PremiumRadioButton,
    SocialRadioButton,
  },
  data() {
    return {
      plan_on_driving: null,
      activePlan: '',
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
      selectedValue: '',
      workspace: null,
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
    headingsWorkspaces() {
      return this.workspaces.map((el) => el.title)
    },
  },
  async created() {
    await this[action.GET_WORKSPACES]()
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },
    changeValue(newValue) {
      this.selectedValue = newValue
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
</style>

<style>
.input-field > input {
  width: 475px;
}

.selected > .radio-description {
  color: var(--primary-text-color);
}
</style>
