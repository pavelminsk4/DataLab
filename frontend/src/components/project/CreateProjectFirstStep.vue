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
        v-for="(item, index) in tests"
        :key="index"
        class="radio-button"
        :label="item.test"
        :value="selectedValue"
        :checked="item"
        @change="changeValue(item)"
      >
        <template v-slot:default> {{ item.test }} </template>
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

export default {
  name: 'CreateProjectFirstStep',
  components: {
    BaseInput,
    BaseSelect,
    BaseRadio,
  },
  data() {
    return {
      plan_on_driving: null,
      activePlan: '',
      tests: [{test: 24}, {test: 36}, {test: 48}],
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
    ...mapActions([action.TEST, action.GET_WORKSPACES]),
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },
    changeValue(newValue) {
      this[action.TEST](newValue)
      this.selectedValue = newValue
    },
    async test() {
      await this[action.TEST](this.workspace)
    },
    navigateToOrder(orderId) {
      this.$router.push({name: 'CreateProjectScreen2', query: {orderId}})
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
</style>

<style>
.input-field > input {
  width: 475px;
}
</style>
