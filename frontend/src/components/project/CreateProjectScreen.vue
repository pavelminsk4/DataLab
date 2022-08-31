<template>
  <MainLayout>
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
        </div>
        <BaseButton class="next-button">Next</BaseButton>
      </div>
    </div>
    <div class="hint">Name the project and choose source Type</div>

    <section class="form-section">
      <div>
        <h4 class="project-name">Name</h4>
        <BaseInput class="input-field" :placeholder="'Project Name'" />

        <h4 class="project-name">Workspace</h4>
        <BaseSelect class="select" />

        <h4 class="project-name">Description</h4>
        <textarea
          class="description-field"
          placeholder="Some words about your project"
        />
      </div>
    </section>
  </MainLayout>
</template>

<script>
import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'

import BaseInput from '@components/BaseInput'
import MainLayout from '@components/layout/MainLayout'
import BaseButton from '@components/buttons/BaseButton'
import BaseSelect from '@/components/BaseSelect'

export default {
  name: 'CreateProjectScreen',
  components: {
    BaseSelect,
    BaseInput,
    BaseButton,
    MainLayout,
    ArrowLeftIcon,
  },
  methods: {
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },
  },
}
</script>

<style scoped>
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
}

.form-section {
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
